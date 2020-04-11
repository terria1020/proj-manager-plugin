# proj-manager-plugin
Sublime Text 3 + MinGW 개발환경에서 개발 시 bin/ , header/ 폴더를 만들어주고, build.bat를 생성해주는 플러그인

> 파일들을 Sublime Text 3 \ Data \ Packages \ User 폴더에 넣을 것.

>> 프로젝트(소스 파일)이 띄워져 있는 곳에서, 단축키 Ctrl+F1키를 누를 시
>> bin/(바이너리 파일이 들어가는 폴더)
>> header/(헤더 파일이 들어가는 폴더)
>> 가 생성되고, mingw-gcc를 실행시킬 빌드 시스템으로부터 실행될 build.bat파일이 만들어집니다.

>> 단축키를 이용하지 않고 사용 시, Ctrl + `를 이용하여 커맨드 창을 여신 뒤,
view.run_command('proj_manager')
>> 를 실행해주시면 되겠습니다.

>>> 빌드 내용 중 프로그램 생성 이름(output), mingw 경로, gcc/g++ 이용 여부, 빌드 타겟 수정 등
>>> 빌드에 필요한 내용은 수정하셔서 사용하시면 됩니다.


> 직접 build.bat를 실행하셔서 빌드하셔도 되고,
> Tools-Build System-New Build System

{
	"shell_cmd": "경로\build.bat"
}


>> 를 생성하셔서 Sublime Text 3 \ Data \ Packages \ User 에 원하는 빌드 시스템 이름으로 저장해주시면 됩니다.

.c나 cpp파일에서 명령어 사용 시 header/소스.h 파일이 작성되는 명령어를 추가하였습니다.
단축키는 Ctrl+F3 / 명령어는 view.run_command('class_manager')

#made by terria1020 / https://terria1020.blogspot.com/
