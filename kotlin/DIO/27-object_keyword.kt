package me.dio.object_classes

// object expression
fun rentPrice(standardDays: Int, festivityDays: Int, specialDays: Int): Unit { 
    val dayRates = object {	// creates an object that storages values
        var standard: Int = 30 * standardDays
        var festivity: Int = 50 * festivityDays
        var special: Int = 100 * specialDays
    }

    val total = dayRates.standard + dayRates.festivity + dayRates.special

    println("Total price: $$total")                                              

}

// object declaration
object DoAuth {                                                 //1 
    fun takeParams(username: String, password: String) {        //2 
        println("input Auth parameters = $username:$password")
    }
}

// companion object
class BigBen {                                  
    companion object Bonger {	// with this you can call a fun without instanceate an object   
        fun getBongs(nTimes: Int) {             
            for (i in 1 .. nTimes) {
                print("BONG ")
            }
        }
    }
}

fun main() {
    rentPrice(10, 2, 1)      
    DoAuth.takeParams("foo", "qwerty")
    BigBen.getBongs(3)
}
