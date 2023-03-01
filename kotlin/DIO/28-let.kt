package me.dio.let.kt

fun customPrint(s: String) {
    print(s.uppercase())	// uppercases the string
}

fun main() {
    val empty = "test".let {               // creates a variable and executes code
        customPrint(it)                    
        it.isEmpty()	// let always returns something in the end
    }
    println(" is empty: $empty")


    fun printNonNull(str: String?) {
        println("Printing \"$str\":")

        str?.let {                         // safe call (executes only if str is not null)
            print("\t")
            customPrint(it)
            println()
        }
    }

    fun printIfBothNonNull(strOne: String?, strTwo: String?) {
        strOne?.let { firstString ->       // 5 
            strTwo?.let { secondString ->
                customPrint("$firstString : $secondString")
                println()
            }
        }
    }

    printNonNull(null)
    printNonNull("my string") 
    printIfBothNonNull("First","Second") 
}
