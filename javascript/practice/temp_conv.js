function celsius(temp){
	const fahrenheit = (temp/5) * 9 + 32;
	const kelvin = temp + 273;
	return [fahrenheit, kelvin];
};

function fahrenheit(temp){
	const celsius = (temp - 32) * 5 / 9;
	const kelvin = ((temp - 32) / 9 ) * 5 + 273;
	return [celsius, kelvin];
};

function kelvin(temp){
	const celsius = temp - 273;
	const fahrenheit = ((temp - 273) / 5) * 9 + 32;
	return [celsius, fahrenheit]; 
};

