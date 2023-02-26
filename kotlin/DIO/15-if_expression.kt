package me.dio.if_expression.kt 

fun main(){
    fun greater(a: Int, b:Int): Int = if (a > b) a else b	// if in one line
    
    println(greater(10, 20))
}
