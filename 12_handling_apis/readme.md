# 📌 API Handling in Python  

## 🚀 Introduction  
APIs (Application Programming Interfaces) allow applications to communicate with each other. In Python, the **requests** module is widely used for making HTTP requests and handling API responses efficiently.  

In this guide, we’ll explore:  
✔ What APIs are and how they work.  
✔ How to make API calls using `requests.get()`.  
✔ Handling API responses and extracting JSON data.  
✔ Exception handling for API failures.  
✔ Practical examples using **FreeAPI** to fetch **random user data** and **YouTube channel details**.  

---

## 🔹 What is an API?  
An **API (Application Programming Interface)** is a set of rules that allows different software applications to communicate with each other. APIs expose endpoints (URLs) that applications can interact with using HTTP methods like:  

- `GET` → Retrieve data from the API.  
- `POST` → Send data to the API.  
- `PUT` → Update existing data.  
- `DELETE` → Remove data.  

### 📌 Types of APIs  
1️⃣ **Public APIs** – Open and free to use (e.g., FreeAPI, OpenWeather, etc.).  
2️⃣ **Private APIs** – Restricted access, used within organizations.  
3️⃣ **REST APIs** – Web-based APIs that follow **RESTful** architecture.  
4️⃣ **GraphQL APIs** – A modern alternative to REST for fetching precise data.  

---

## 🔹 Python API Handling with `requests`  

### ✅ Installing `requests` Module  
The `requests` library is a popular Python package for making HTTP requests. To install it, run:  
```bash
pip install requests
```

### ✅ Making API Calls using `requests.get()`  
The `requests.get(url)` function sends an HTTP **GET request** to fetch data from an API.  

Example:  
```python
import requests  

response = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random")  
print(response.status_code)  # 200 (Success)
```

### ✅ Handling API Responses (JSON)  
Most APIs return data in **JSON format** (JavaScript Object Notation). We can parse it using `.json()`.  

Example:  
```python
data = response.json()  
print(data)  
```

---

## 🔹 Example 1: Fetching Random User Data  

The following script interacts with **FreeAPI** to fetch a **random user's information**, including their username and country.  

### 📝 Code Explanation  
```python
import requests  

def fetch_random_user_freeapi():  
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"  # API endpoint  
    response = requests.get(url)  # Sending a GET request  
    data = response.json()  # Parsing JSON response  

    if data["success"] and "data" in data:  # Checking API success response  
        user_data = data["data"]  
        username = user_data["login"]["username"]  
        country = user_data["location"]["country"]  
        return username, country  
    else:  
        raise Exception("Failed to fetch user data.")  # Handling API failure  

def main():  
    try:  
        username, country = fetch_random_user_freeapi()  
        print(f"Username: {username} \nCountry: {country}")  
    except Exception as e:  
        print(str(e))  # Error handling  

if __name__ == "__main__":  
    main()
```

### 🔹 Key Concepts Used  
| **Keyword** | **Explanation** |  
|------------|----------------|  
| `import requests` | Imports the `requests` module for making HTTP API requests. |  
| `requests.get(url)` | Sends a `GET` request to the given API URL. |  
| `response.json()` | Parses the API response into a Python dictionary. |  
| `if data["success"] and "data" in data:` | Checks if the API response is successful. |  
| `raise Exception("Failed to fetch user data.")` | Raises a custom error if the API fails. |  
| `try-except` | Handles errors gracefully. |  

---

## 🔹 Example 2: Fetching YouTube Channel Details  

This script fetches **YouTube channel information** using FreeAPI.  

### 📝 Code Explanation  
```python
import requests  

def fetch_youtube_channel_details():  
    api_url = "https://api.freeapi.app/api/v1/public/youtube/channel"  
    api_response = requests.get(api_url)  # Sending API request  
    response_data = api_response.json()  # Converting response to JSON  

    if response_data["success"] and "data" in response_data:  # Checking success  
        channel_data = response_data["data"]  
        channel_title = channel_data["info"]["snippet"]["title"]  
        channel_description = channel_data["info"]["snippet"]["description"]  
        return channel_title, channel_description  
    else:  
        raise Exception("Failed to fetch YouTube channel details")  

def main():  
    try:  
        channel_title, channel_description = fetch_youtube_channel_details()  
        print(f"Channel Title: {channel_title} \nChannel Description: {channel_description}")  
    except Exception as error:  
        print(str(error))  

if __name__ == "__main__":  
    main()
```

### 🔹 Key Concepts Used  
| **Keyword** | **Explanation** |  
|------------|----------------|  
| `requests.get(api_url)` | Fetches YouTube channel data using an API request. |  
| `api_response.json()` | Converts API response into a Python dictionary. |  
| `if response_data["success"] and "data" in response_data:` | Ensures the API request was successful. |  
| `raise Exception("Failed to fetch YouTube channel details")` | Custom error handling for failed requests. |  
| `try-except` | Catches and handles errors to prevent program crashes. |  

---

## 🔹 Exception Handling in API Calls  

APIs can fail due to various reasons:  
✔ Network issues.  
✔ API endpoint changes.  
✔ Invalid API key or request parameters.  
✔ API server downtime.  

### ✅ Best Practices for Exception Handling  
🔹 Use `try-except` to prevent crashes.  
🔹 Check API response status codes (`200` for success).  
🔹 Validate JSON response before accessing data.  
🔹 Use `raise Exception("Custom Error Message")` for meaningful errors.  

Example:  
```python
try:  
    response = requests.get("https://api.invalid-url.com")  
    response.raise_for_status()  # Raises an error for bad responses  
except requests.exceptions.RequestException as e:  
    print(f"API Request Failed: {e}")  
```