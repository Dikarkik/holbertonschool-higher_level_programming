#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
	console.log(1);
} else if (number <= 1) {
	console.log(1);
} else {

	function fac(num) {
		if (num === 1)
			return (num);
		let next = fac(num - 1);
		return (num * next);
	}
	console.log(fac(number));
}
