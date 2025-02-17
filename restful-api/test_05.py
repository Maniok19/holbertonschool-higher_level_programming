#!/usr/bin/python3
import requests

BASE_URL = "http://127.0.0.1:5000"  # Adresse de l'API Flask

# Utilisateurs de test
basic_auth_user = ("user1", "password")
basic_auth_admin = ("admin1", "password")

jwt_user_credentials = {"username": "user1", "password": "password"}
jwt_admin_credentials = {"username": "admin1", "password": "password"}

def test_basic_auth():
    print("Testing Basic Authentication...")

    # Test sans authentification
    response = requests.get(f"{BASE_URL}/basic-protected")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Test avec utilisateur valide
    response = requests.get(f"{BASE_URL}/basic-protected", auth=basic_auth_user)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["message"] == "Basic Auth: Access Granted"

    print("Basic Authentication tests passed!")


def test_jwt_auth():
    print("Testing JWT Authentication...")

    # Test login utilisateur
    response = requests.post(f"{BASE_URL}/login", json=jwt_user_credentials)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    user_token = response.json().get("access_token")
    assert user_token, "JWT token not received for user"

    # Test login admin
    response = requests.post(f"{BASE_URL}/login", json=jwt_admin_credentials)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    admin_token = response.json().get("access_token")
    assert admin_token, "JWT token not received for admin"

    # Test accès JWT protégé sans token
    response = requests.get(f"{BASE_URL}/jwt-protected")
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Test accès JWT protégé avec token utilisateur
    headers = {"Authorization": f"Bearer {user_token}"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["message"] == "JWT Auth: Access Granted"

    print("JWT Authentication tests passed!")
    return user_token, admin_token


def test_role_based_access(user_token, admin_token):
    print("Testing Role-Based Access Control...")

    # Test accès admin-only avec token utilisateur
    headers_user = {"Authorization": f"Bearer {user_token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers_user)
    assert response.status_code == 403, f"Expected 403, got {response.status_code}"
    assert response.json()["error"] == "Admin access required"

    # Test accès admin-only avec token admin
    headers_admin = {"Authorization": f"Bearer {admin_token}"}
    response = requests.get(f"{BASE_URL}/admin-only", headers=headers_admin)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["message"] == "Admin Access: Granted"

    print("Role-Based Access Control tests passed!")


if __name__ == "__main__":
    print("Starting tests...\n")

    # Tester Basic Authentication
    test_basic_auth()

    # Tester JWT Authentication et récupérer les tokens
    user_token, admin_token = test_jwt_auth()

    # Tester le contrôle d'accès basé sur les rôles
    test_role_based_access(user_token, admin_token)

    print("\nAll tests passed successfully!")
