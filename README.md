# API'S
### Requesting an api in python
```python
import requests
import json
# get request

post_codes_req = requests.get("https://api.postcodes.io/postcodes/sl61tx")

print(post_codes_req) # <Response [200]>
print(post_codes_req.status_code) # 200
print(post_codes_req.content) # turns content from URI, as bytes
print(post_codes_req.json()) # turns content into python dict
print(type(post_codes_req.json())) # shows the type is now dict

# POST request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# Pokermon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/squirtle")
print(pokemon_req.json())

bbc_request = requests.get("https://bbc.com/")
print(bbc_request.content)
```
#### What are APIs
APIs (Application Programming Interfaces) are sets of rules and protocols that allow different software applications to communicate and interact with each other. They define how different components of software systems should interact, enabling seamless integration and data exchange between applications.

#### How are APIs used and why are they so popular?
APIs are used to enable functionality and data sharing between different applications, systems, or services. They allow developers to access and utilize pre-built functionalities, services, or data provided by other applications or platforms. APIs are popular because they simplify development, enhance interoperability, promote modularity, and enable developers to leverage the capabilities of existing software components without having to build everything from scratch.

#### What is a REST API? What makes an API RESTful?
A REST API (Representational State Transfer API) is an architectural style for designing networked applications. REST is based on a set of principles and constraints that emphasize simplicity, scalability, and statelessness.

Stateless: The server should not store any client state between requests. Each request from the client should contain all the necessary information to understand and process the request.

Client-Server Architecture: The client and server are separate entities that communicate over the network. They have distinct responsibilities, where the client is responsible for the user interface and the server handles the storage and processing of data.

Uniform Interface: The API should have a uniform and consistent interface for accessing and manipulating resources. It typically includes the use of standard HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform operations on resources.

Resource-Oriented: Resources are the key concept in a RESTful API. Each resource should have a unique identifier (URI) and be accessible through that identifier. Resources are manipulated using representations such as JSON or XML.

Cacheable: Responses from the server can be cached on the client side or intermediary servers (such as CDNs) to improve performance and reduce the load on the server.

Layered System: The architecture can be composed of multiple layers, where each layer provides a specific set of functionality. The client interacts with the API without being aware of the underlying layers.

Code on Demand in RESTful: APIs allows the server to send executable code to the client, enhancing its functionality dynamically.

#### What is HTTP?
HTTP (Hypertext Transfer Protocol) is an application protocol that defines the format and rules for communication between web browsers (clients) and web servers. It stands for Hypertext Transfer Protocol. It is the foundation of data communication on the World Wide Web and is used for retrieving resources (such as HTML pages, images, etc.) and interacting with web services.

#### What is HTTPS?
HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP. It provides encrypted communication over a computer network, typically the internet. HTTPS uses SSL (Secure Sockets Layer) or TLS (Transport Layer Security) protocols to establish a secure connection between the client and the server, ensuring the confidentiality and integrity of data exchanged.

#### HTTP Request structure
An HTTP request consists of:
Request line: Contains the HTTP method (GET, POST, PUT, etc.), the target URL or URI, and the HTTP version.
Headers: Additional metadata about the request, such as content type, authentication details, caching directives, etc.
Body (optional): Contains additional data sent with the request, such as form data or JSON payload.

