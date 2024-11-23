import numpy as np

def calculate_orbital_elements(position, velocity, mu=398600.4418):
    """
    Calculates Keplerian orbital elements from position and velocity vectors.

    Parameters:
    position (array): Position vector (km) [x, y, z].
    velocity (array): Velocity vector (km/s) [vx, vy, vz].
    mu (float): Standard gravitational parameter for Earth (km^3/s^2).

    Returns:
    dict: Orbital elements (semi-major axis, eccentricity, inclination, etc.).
    """
    # Calculate magnitudes
    r = np.linalg.norm(position)
    v = np.linalg.norm(velocity)

    # Angular momentum vector
    h = np.cross(position, velocity)
    h_mag = np.linalg.norm(h)

    # Inclination
    inclination = np.degrees(np.arccos(h[2] / h_mag))

    # Node vector
    k = np.array([0, 0, 1])  # Z-axis
    n = np.cross(k, h)
    n_mag = np.linalg.norm(n)

    # Longitude of ascending node
    if n_mag != 0:
        raan = np.degrees(np.arccos(n[0] / n_mag))
        if n[1] < 0:
            raan = 360 - raan
    else:
        raan = 0

    # Eccentricity vector
    e_vec = (1 / mu) * (np.cross(velocity, h) - mu * (position / r))
    eccentricity = np.linalg.norm(e_vec)

    # Argument of periapsis
    if n_mag != 0 and eccentricity != 0:
        arg_periapsis = np.degrees(np.arccos(np.dot(n, e_vec) / (n_mag * eccentricity)))
        if e_vec[2] < 0:
            arg_periapsis = 360 - arg_periapsis
    else:
        arg_periapsis = 0

    # True anomaly
    if eccentricity != 0:
        true_anomaly = np.degrees(np.arccos(np.dot(e_vec, position) / (eccentricity * r)))
        if np.dot(position, velocity) < 0:
            true_anomaly = 360 - true_anomaly
    else:
        true_anomaly = 0

    # Semi-major axis
    energy = (v**2 / 2) - (mu / r)
    if energy != 0:
        semi_major_axis = -mu / (2 * energy)
    else:
        semi_major_axis = np.inf  # Parabolic orbit

    return {
        "semi_major_axis": semi_major_axis,
        "eccentricity": eccentricity,
        "inclination": inclination,
        "raan": raan,
        "arg_periapsis": arg_periapsis,
        "true_anomaly": true_anomaly,
    }

def validate_trajectory(predicted_positions, actual_positions):
    """
    Compares predicted trajectories with actual data.

    Parameters:
    predicted_positions (array): Predicted positions (Nx3).
    actual_positions (array): Actual positions (Nx3).

    Returns:
    float: RMS error between predicted and actual positions.
    """
    errors = np.linalg.norm(predicted_positions - actual_positions, axis=1)
    rms_error = np.sqrt(np.mean(errors**2))
    return rms_error

if __name__ == "__main__":
    # Example position and velocity vectors
    position = np.array([7000, 0, 0])  # km
    velocity = np.array([0, 7.5, 0])   # km/s

    # Calculate orbital elements
    elements = calculate_orbital_elements(position, velocity)
    print("Orbital Elements:")
    for key, value in elements.items():
        print(f"{key}: {value:.4f}")

    # Example trajectory validation
    predicted_positions = np.array([
        [7000, 0, 0],
        [6999, 10, 5],
        [6998, 20, 10],
    ])
    actual_positions = np.array([
        [7000, 0, 0],
        [6999, 10.5, 5.1],
        [6997.5, 20.2, 10.3],
    ])
    rms_error = validate_trajectory(predicted_positions, actual_positions)
    print(f"\nRMS Error in Trajectory: {rms_error:.4f} km")
