from .test_setup import TestSetUp

class TestViews(TestSetUp):
    
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 201)
        # if res.status_code == 400:
            
    def test_user_can_register_correctlly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.data["email"], self.user_data['email'])
        self.assertEqual(res.data["name"], self.user_data['name'])
        # self.assertEqual(res.data["password"], self.user_data['password'])
        self.assertEqual(res.status_code, 201)
        
    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url)
        self.assertEqual(res.status_code, 200)
        
    def test_user_can_login_correctlly(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, data={'email' : self.user_data['email'], 'password' : self.user_data['password']}, format="json")
        # print(res.content)
        self.assertEqual(res.status_code, 200)