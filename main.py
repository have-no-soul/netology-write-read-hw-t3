import os


def create_new_file(folder_name):
	file_list = os.listdir(folder_name)
	combined_list = []

	for file in file_list:
		with open(folder_name + "/" + file) as f:
			file_lines = f.readlines()
			combined_list.append([file, len(file_lines), file_lines])

	sorted_list = sorted(combined_list, key=lambda x: x[2], reverse=True)

	with open(folder_name + '/new.txt', "w+") as new_file:
		for item in sorted_list:
			new_file.write(f'{item[0]}\n')
			new_file.write(f'{item[1]}\n')
			for line in item[2]:
				new_file.write(line.strip() + '\n')


create_new_file('files')
