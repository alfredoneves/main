package me.dio.loops_int.kt 

fun main(){
    for (i in 0..3) {	// includes 3
        print(i)
    }
    println("")
    
    for (i in 0 until 3){ // excludes 3
        print(i)
    }
    println("")
    
    for (i in 0..10 step 2){	// jumps 2
        print(i)
    }
    println("")
    
    for (i in 3 downTo 0){	// regressive
        print(i)
    }
}
