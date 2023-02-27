package me.dio.mapXflat_map.kt 



fun main(){
    val fruits_bag: List<String> = listOf("banana", "apple", "orange")
	val clothes_bag: List<String> = listOf("shirt", "jeans")
	val cart = listOf(fruits_bag, clothes_bag)	// creates a list of lists
	val map_bag = cart.map {it}	// maintains the lists inside the list
	val flat_map_bag = cart.flatMap {it}	// unifies the lists
    
    println(map_bag)
    println(flat_map_bag)
}
