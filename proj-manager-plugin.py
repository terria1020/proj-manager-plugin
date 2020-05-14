import sublime
import sublime_plugin
import os


#setting basic path, name
#if you use other unnormal path, edit self

user_path = "C:\\Users\\"
username = "Cyber"
#MinGW\bin\ path put here
#[edit self]
mingw_path = user_path + username + "\\Downloads\\MinGW\\MinGW\\bin"
basic_build_system_path = user_path + username + "\\Downloads\\Sublime3\\Data\\Packages\\User\\mingw-build.sublime-build"
output_file_name = "main.exe"


#if use g++, remove comment

#build_sys = "gcc.exe"
build_sys = "g++.exe"


#build_target setting. other set : build_target = <source>, <source2>, ..
#[edit self]

build_target = "*.cpp"
#build_target = "*.c"



class ProjManagerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
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

		f.write("set tgpath=" + path + "\n");
		f.write("cd " + mingw_path + "\n\n")
		f.write("if exist %tgpath%bin\\" + output_file_name + " (\n")
		f.write("\tdel %tgpath%bin\\" + output_file_name + "\n")
		f.write(")\n\n")
		f.write(build_sys + " -o %tgpath%bin\\" + output_file_name + " %tgpath%" + build_target + "\n\n")
		f.write("if exist %tgpath%bin\\" + output_file_name + " (\n")
		f.write("\techo build success.\n")
		f.write(")\n")

		f.close()

class ClassManagerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		get_path = self.view.file_name()
		indextemp = 0
		t_list = get_path.split('\\')
		for i in t_list:
			indextemp = len(i)
		section_text = t_list[-1].split(".")
		text_len = len(section_text[-1])
		hpath = get_path[0:-(indextemp)] + "header\\" + section_text[0] + ".h"

		f = open(hpath, 'w')

		f.write("#pragma once\n\n")

		f.write("class " + section_text[0] + " {\n")
		f.write("private:\n")
		f.write("\t\n")
		f.write("public:\n")
		f.write("\t" + section_text[0] + "();\n")
		f.write("\t~" + section_text[0] + "();\n")
		f.write("};")

		f.close()

		self.view.insert(edit, 0, "#include \"" + "header\\" + section_text[0] + ".h\"\n\n"
			+ section_text[0] + "::" + section_text[0] + "() {\n\t\n}\n"
			+ section_text[0] + "::~" + section_text[0] + "() {\n\t\n}\n")

class MingwBuildSystemPatchManagerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		get_path = self.view.file_name()
		indextemp = 0
		t_list = get_path.split('\\')
		for i in t_list:
			indextemp = len(i)
		path = get_path[0:-(indextemp)]

		temp = "\t\"shell_cmd\": \"" + path + "build.bat\"\n"
		maintxt = temp.replace("\\", "\\\\");

		f = open(basic_build_system_path, "w")
		f.write("{\n")
		f.write(maintxt)
		f.write("}")
		f.close()