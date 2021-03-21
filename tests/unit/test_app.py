from project.models import User, Report

def test_new_user():
    # Given a User model
    # When a new user is created
    # Then check the email, hashed password and first_name
    user = User('jfkennedy@email.com', 'John')

    #User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
    assert user.email == 'jfkennedy@email.com'
    assert user.first_name == 'John'



# if __name__ == '__main__':
#     pytest.main()
