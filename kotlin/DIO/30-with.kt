package me.dio.with.kt 

class Configuration(val host: String, val port: Int)

fun main() {
    val host: String = "127.0.0.1"
    val port: Int = 80
    val config: Configuration = Configuration(host, port)
    
    with (config) {
        println("$host:$port")
    }
    
   	// alternative
   	config.run {
        println("$host:$port")
    }
    
    // traditional
    println("${config.host}:${config.port}")
}
