package me.dio.run.kt 

fun main() {
    fun get_nullable_length(ns: String?): Int {
        println("testing: $ns")
        return ns?.run {	// enters this if ns is not null
        	println("is $ns empty? " + isEmpty())	// with run you don't need to make this.isEmpty() 
            println("length: $length")
            length
        } ?: 0	// returns 0 if ns is null
    }
    
    println(get_nullable_length(null))
    println(get_nullable_length(""))
    println(get_nullable_length("ana"))
    
}
