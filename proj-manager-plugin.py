import sublime
import sublime_plugin
import os

class ProjManagerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#MinGW\bin\ path put here
		mingw = "C:\\Users\\Cyber\\Downloads\\MinGW\\MinGW\\bin"	
		#output file name
		output = "main.exe"	
		#if use g++, remove comment
		#build_sys = "g++"
		build_sys = "gcc"
		#build_target = "*.cpp"
		build_target = "*.c"


		get_path = self.view.file_name()
		indextemp = 0
		t_list = get_path.split('\\')
		for i in t_list:
			indextemp = len(i)
		path = get_path[0:-(indextemp)]

		if not(os.path.isdir(path + "bin")):
			os.makedirs(os.path.join(path + "bin"))

		if not(os.path.isdir(path + "header")):
			os.makedirs(os.path.join(path + "header"))

		f = open(path + "build.bat", 'w')
		f.write("@echo off\n\n")

		f.write("cd " + mingw + "\n\n")
		f.write("if exist " + path + "bin\\" + output + "(\n")
		f.write("\tdel " + path + "bin\\" + output + "\n")
		f.write(")\n\n")
		f.write(build_sys + " -o " + path + "bin\\" + output + " " + path + "\\" + build_target + "\n\n")
		f.write("if exist " + path + "bin\\" + output + "(\n")
		f.write("\techo build success.\n")
		f.write(")\n")

		f.close()