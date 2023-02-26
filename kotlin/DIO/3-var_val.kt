package me.dio.var_val.kt

fun main(){
	val test: Int
	// println($test) uncomment to check error
	val light: String = "off"	// val is used to imutable values
	var code: Int	// var is used to mutable values
	if (light == "off"){
		code = 0
	} else {
		code = 1
	}
	println("code: $code")
}
