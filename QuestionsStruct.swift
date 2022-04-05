//
//  Questions.swift
//  ISpeSmartWatch
//
//  Created by Joon-Erik Sæther on 14/03/2022.
//
import Foundation

struct Questions: Codable, Identifiable {
	let id: Int
	let parentID: Int?
	let order: Int?
	let group: String?
	let type: String?
	let text: String?
	let subQuestions: [Questions]?
}
