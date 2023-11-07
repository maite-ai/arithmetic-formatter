def arithmetic_arranger(problems, show_results=False):
	
	# Only five or less problems, otherwise throws an error
	if len(problems) > 5:
		return "Error: Too many problems."

	arranged_problems = {
		"top": [],
		"bottom": [],
		"line": [],
		"result": []
	}

	for problem in problems:
		operand_a, operator, operand_b = problem.split()

		# Check if operator is valid
		if operator not in ["+", "-"]:
			return "Error: Operator must be '+' or '-'."

		# Check whether the problem only contains numbers
		if not operand_a.isdecimal() or not operand_b.isdecimal():
			return "Error: Numbers must only contain digits."

		# Check if numbers are four digits longer
		if len(operand_a) > 4 or len(operand_b) > 4:
			return "Error: Numbers cannot be more than four digits."

		# Determine the length of the space of this problem
		length = max(len(operand_a), len(operand_b)) + 2

		# Add operands and lines to the appropiate lists
		arranged_problems["top"].append(operand_a.rjust(length))
		arranged_problems["bottom"].append(operator + operand_b.rjust(length - 1))
		arranged_problems["line"].append("-"* length)

		# Calculate the results
		if show_results:
			result = str(eval(problem))
			arranged_problems["result"].append(result.rjust(length))

	arranged_top = "    ".join(arranged_problems["top"])
	arranged_bottom = "    ".join(arranged_problems["bottom"])
	arranged_line = "    ".join(arranged_problems["line"])

	if show_results:
		arranged_result = "    ".join(arranged_problems["result"])
		return f"{arranged_top}\n{arranged_bottom}\n{arranged_line}\n{arranged_result}"
	else:
		return f"{arranged_top}\n{arranged_bottom}\n{arranged_line}"