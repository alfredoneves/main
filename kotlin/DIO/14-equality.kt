package me.dio.equality.kt 

fun main(){
    val authors = setOf("Dostoiévski", "Shakespeare")	// set eliminates duplicates
    val writers = setOf("Shakespeare", "Dostoiévski")
    
    println(authors == writers)	// structure comparison
    println(authors === writers)	// memory reference comparison
}
