def password_verification():
    while True:
        password = input("Enter Password: ")
        verify_password = input("Verify Password: ")
        if password == verify_password:
            print("Password verified successfully!")
            break
        else:
            print("Password verification failed. Retry")
password_verification()