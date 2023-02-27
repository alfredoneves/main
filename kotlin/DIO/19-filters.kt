package me.dio.filters.kt 

val numbers: List<Int> = listOf(-1, 0, 1, 2, 3, 4, 5)

fun main(){
    val positives: List<Int> = numbers.filter {x -> x > 0}	// filter 1
    val negatives: List<Int> = numbers.filter {it < 0}	// filter 2
    val doubled: List<Int> = numbers.map {x -> x * 2}	// map applies a function to a list
    val tripled: List<Int> = numbers.map {it * 3}	// map 2
    val any_lower_3: Boolean = numbers.any {it < 3}	// verifies a condition
    println("numbers: $numbers")
    println("positives: $positives")
    println("negatives: $negatives")
    println("doubled: $doubled")
    println("tripled: $tripled")
    println("there is any number lower than 3? $any_lower_3")
}
