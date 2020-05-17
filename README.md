# proj-manager-plugin
## 플러그인 설명
C/C++ 개발 환경에서 개발 편의성을 위해 사용하는 플러그인.  
프로젝트 폴더 자동생성, 생성하는 클래스에 따른 헤더파일 생성/분리 자동화,  
프로젝트 폴더에 자동 작성된 배치 파일을 이용한 빌드 시 현재 폴더에 따른 빌드시스템 최신화  

## 개발 목적
Sublime Text 3 + Mingw를 이용한 프로그래밍 연습, 개발 등 C/C++ 개발 시 개발 환경에 따른 빌드 시스템을 구축하기 번거롭고,  
클래스 작성 시 IDE같은 통합 개발 환경의 개발 편의성을 따라가지 못해 불편함이 있다.  
그 점을 개선하기 위해 다음과 같은 플러그인을 만들게 되었다.  

## 적용법
파일들을 Sublime Text 3 \ Data \ Packages \ User 폴더에 넣을 것.  
**완전 자동화는 아니기 때문에, 플러그인의 메인이 되는 proj-manager-plugin.py의 전역 변수들에서  
프로그램 생성 이름(output), mingw 경로, gcc/g++ 이용 여부, 빌드 타겟 수정 등  
각자 자신의 컴퓨터 환경에 맞게 경로 등을 수정하고 사용하면 된다.**  

## 단축키
단축키 파일을 정상적으로 적용 폴더에 넣으면, 다음과 같은 단축키를 사용할 수 있다.
```
Ctrl + F1 : 현재 보고있는 파일의 위치에 프로젝트 단위 폴더 생성
다음과 같은 세 개의 파일·폴더가 생성된다.
	bin/
	header/
	build.bat

Ctrl + F3 : 현재 보고있는 cpp파일의 이름을 가져와 클래스 헤더 파일을 작성한다.
	헤더파일 작성은 물론 현재 보고있는 cpp파일에도 클래스의 기본 형태가 작성되니,
	클래스.cpp 파일을 새로 생성 후 바로 단축키를 사용하면 되겠다.
	Ctrl + F1과 연동하여 사용한다.

Ctrl + F5 : 현재 보고 있는 파일의 폴더 위치를 기반으로 서브라임 빌드 시스템 파일을 수정한다.
	서브라임 빌드 파일은 Ctrl + F1 단축키를 이용하여 생성된 build.bat를 실행하게 하는 것으로,
	현재 보고있는 파일의 경로를 찾아 빌드 시스템에 경로\build.bat를 작성하는 것이다.
	Ctrl + F1과 연동하여 사용한다.
```

만약 단축키를 사용하지 않고 커맨드를 직접 실행하고자 하면  
Ctrl + \`를 이용하여 커맨드 창을 여신 뒤,
```python
view.run_command('proj-manager')
view.run_command('class_manager')
view.run_command('mingw_build_system_patch_manager')
```
필요한 커맨드를 실행시키시면 되겠습니다.


## 사용 예
Ctrl + F1 단축키 사용시 :   
![image1](https://1.bp.blogspot.com/-6Qym94FMcT0/XsFEVWdheTI/AAAAAAAABDg/UJFXiu_iNEEP32amC0eWTp7nfXHaf5WTwCK4BGAsYHg/s320/1.PNG)  
Ctrl + F3 단축키 사용시 :   
![image2](https://1.bp.blogspot.com/-cXVqEqJqlaM/XsFEw4zUYLI/AAAAAAAABD0/hh5r7PvNXEk7aiH5KNLB4HpoAJ6FQCjoQCK4BGAsYHg/2.png)  
Ctrl + F5 단축키 사용시 :   
![image3](https://1.bp.blogspot.com/-9IPx1kwKjN0/XsFFaYS7JPI/AAAAAAAABEU/4sjIeRr6BZw_65851cLtVxurnnbvfe_xgCK4BGAsYHg/3.png)  

-----------------------

#made by terria1020 / [blog](https://terria1020.blogspot.com/)
