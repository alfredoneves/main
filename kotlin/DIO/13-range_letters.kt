package me.dio.range_letters.kt 

fun main(){
    for (letter in 'a'..'z'){	// single cote is necessary to use range
        print(letter)
    }
    println("")
    
    for (letter in 'z' downTo 'a'){	// downTo works with letters too
        print(letter)
    }
    println("")
    
    val x = 3
    if (x in 0..5){
        print("val $x is in the range 0..5")
    }
}
