package me.dio.do_while.kt 

fun eat_cake(num: Int) = println("eat a cake $num!")
fun bake_cake(num: Int) = println("bake a cake $num!")

fun main(){
    var cakes_eaten: Int = 0
    var cakes_baked: Int = 0
    
    while (cakes_eaten < 5) {
        eat_cake(cakes_eaten)
        cakes_eaten ++
    }
    
    do {	// executes before checking the condition
        bake_cake(cakes_baked)
        cakes_baked ++
    } while (cakes_baked < cakes_eaten)
    println(cakes_eaten)
    println(cakes_baked)
   
}
