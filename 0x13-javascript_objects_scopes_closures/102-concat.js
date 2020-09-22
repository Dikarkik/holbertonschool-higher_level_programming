#!/usr/bin/node

fs = require('fs')

function concatFiles(fileDestiny, file) {
	fs.readFile(file, 'utf-8', function (err, data) {
		if (err) {
			return console.log(err);
		}
		fs.appendFile(fileDestiny, data, function (err, result) {
			if (err) console.log('error', err)
		})
	})
}

let fileA = process.argv[2]
let fileB = process.argv[3]
let fileDestiny = process.argv[4]

concatFiles(fileDestiny, fileA)
concatFiles(fileDestiny, fileB)





// let dataa = fs.readFile(process.argv[2], 'utf-8', function (err, data) {
// 	if (err) {
// 		return console.log(err);
// 	}
// 	return data
// })

// console.log(dataa)

// fs.readFile(process.argv[3], 'utf-8', function (err, data) {
// 	if (err) {
// 		return console.log(err);
// 	}
// 	text += data

// })

// console.log(text)