// Import reqwest
use reqwest::{blocking};

// Add a and b
fn add_two(a: i32, b: i32) -> i32 {
    a + b
}

// Compute the fibonacci number of order n.
fn fibonacci(n: i32) -> i32 {
    if n == 0 || n == 1 {
        return n;
    }

    fibonacci(n - 1) + fibonacci(n - 2)
}

// Ping google.com and return the response.
fn ping_google() -> String {
    let url = "https://google.com";
    let client = reqwest::blocking::Client::new();
    let res = client.get(url).send();
    res.unwrap().text().unwrap()
}

fn main() {
    println!("Hello World!");

    // Get input from the user
    let mut input_text = String::new();
    std::io::stdin().read_line(&mut input_text).expect("Failed to read line");

    // Print the input text to the console
    println!("You typed: {}", input_text);

    // Convert the input text to an integer
    let input_number: i32 = input_text.trim().parse().expect("Please type a number!");

    // Print the input number to the console
    println!("You typed: {}", input_number);

    // Add two numbers
    let sum = add_two(input_number, 42);

    // Print the sum to the console
    println!("The sum is: {}", sum);

    // Print the fibonacci number of order n
    println!("The fibonacci number of order {} is: {}", input_number, fibonacci(input_number));

    // Ping google.com
    println!("The response from google.com is: {}", ping_google());

}
