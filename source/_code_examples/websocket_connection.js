// In Javascript, you can use the built-in WebSocket API like shown below
// https://developer.mozilla.org/en-US/docs/Web/API/WebSocket

const socket = new WebSocket("https://my-kindafax-instance.example.com");

socket.addEventListener("open", event => {

    // When the connection opens. Send a message back to the server.
    socket.send("Hello, World!");
})

socket.addEventListener("message", event => {
    
    // Each time the client receives a message, log it to the console
    console.log(event.data);
})

socket.addEventListener("close", event => {

    // Log a message when the connection closes
    console.log("WebSocket Connection Closed");
})

socket.addEventListener("error", error => {

    // Log when the connection errors.
    console.error("Error with socket", error);
})