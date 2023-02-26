package me.dio.classes.kt

class Customer	// creates a class
class Contact(val id: Int, var email: String)
fun main(){
    val customer = Customer()	// instances the class
    val contact = Contact(1, "ana@gmail.com")
    
    println(contact.id)
    println(contact.email)
    contact.email = "ana2@gmail.com"	// the email is var, so it can be changed
    println(contact.email)
    
}
