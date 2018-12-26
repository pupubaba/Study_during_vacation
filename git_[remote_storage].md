# 원격저장소
원격저장소는 인터넷이나 네트워크 어딘가에 있는 저장소를 말한다. 간단히 말해서 다른 사람들과 함께 일한다는 것은 원격저장소를 관리하면서 데이터를 거기에  push하고 pull하는 것이다

### 원격저장소 생성
<code>$ git init "name"</code> 
name이라는 로컬저장소를 생성하는 명령어

<code>$ git init --bare "name"</code> 
작업은 하지 않고 저장만하는 저장소를 생성하는 명령어

<code>$ git remote add "remote_name" "address"</code> 
"address"에 위치한 저장소를 추가하는 명령어로 "remote_name"붙여 사용한다

## Github
### 원격 저장소를 지역 저장소로 복제
<code>$ git clone "address"</code> 
"address"에 위치한 파일을 복제해서 가져옴

<code>$ git checkout "commit_address"</code> 
branch뿐만 아니라 commit으로도 이동가능

### 원격 저장소 만들기
Github도 동일하게 git remote add "remote_name" "address"를 사용하여 저장소 추가

<code>$ git remote remove "remote_name"</code>
"remote_name" 저장소를 제거하는 명령어

<code>$ git push -u "origin" "master"</code>
origin이라는 원격저장소의 master branch에 소스를 업로드하는 명령어

<code>$ git remote -v</code>
전체 저장소의 리스트를 보여주는 명령어

### 원격 저장소와 지역 저장소의 동기화 방법
<code>$ git pull</code>
원격 저장소에 있는 소스를 지역 저장소로 가져오는 명령어

### 로그인 없이 원격 저장소 이용하기
SSH이용하여 로그인 없이 원격 저장소를 이용할 수 있다

<code>$ ssh-keygen</code>
SSH를 통해 다른 컴퓨터에 접속할 수 있는 비밀번호 발급
* .ssh폴더에 id_rsa와 id_rsa.pub 생성
* id_rsa : private key이고 로컬컴퓨터에 저장된다 
* id_rsa.pub : public key이고 서버컴퓨터에 저장되며 로컬컴퓨터에도 저장된다
* github에서 Setting -> SSH and GPG keys에서 New SSH key를 클릭하여 추가한다

## My Server
### 자기 서버에 원격 저장소 만들기
<code>$ git remote add origin ssh://git@"My Sever_address"/"directory_address"/</code>
My Server의 저장소를 추가하는 명령어

### push & pull
위에서 언급한 것과 동일
* push하기전에는 꼭 pull해야함

### 자동로그인(My Server)
<code>$ ssh-keygen -t rsa</code>
rsa암호 방식의 key를 발급하는 명령어
* 생성되는 파일은 Github 로그인 없이 원격 저장소 이용하기와 동일
* Server저장소에 .ssh폴더에 authorized_keys라는 파일을 생성후 id_rsa.pub안에 있는 key를 입력
* <code>$ ssh-copy-id "User_id"@"Server_address"</code>를 입력하여 쉽게 authorized_keys생성 가능