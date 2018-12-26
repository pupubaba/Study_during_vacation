# git의 혁신 branch

## branch란 
여러명의 개발자들이 동시에 다양한 작업을 할 수 있게 만들어 주는 기능이다
각자 독립적인 작업 영역(저장소) 안에서 마음대로 소스코드를 변경할 수 있다 
또한 이렇게 분리된 작업 영역에서 변경된 내용은 나중에 원래의 버전과 비교해서 하나의 새로은 버전으로 만들어 낼 수 있다

## branch 만들기

<code>git branch</code> 
* 현재 branch목록을 확인할 수 있는 명령어

<code>git branch "branch_name"</code>
* branch_name이라는 branch를 만드는 명령어

<code>git checkout "branch_name"</code>
* branch_name의 branch로 이동하는 명령어

<code>git checkout "branch_name"</code>
* 새로운 branch를 생성하고 이동까지 하는 명령어


## branch 정보확인

<code>git log --branches --decorate</code>
* log에 각각의 branch의 commit상태를 표시하는 명령어

<code>git log --branches --decorate --graph</code>
* 위에 명령어 상태에서 그래프를 추가하여 commit상태를 표시하는 명령어

<code>git log --branches --decorate --graph --oneline</code>
* 위에 명령어 상태를 한줄로 표시하는 명령어

<code>git log "branch_name1".."branch_name2"</code>
* branch_name1에는 있지만 branch_name2에는 없는 commit를 표시하는 명령어

<code>git log -p "branch_name1".."branch_name2"</code>
* 소스코드까지 비교하는 명령어

<code>git diff "branch_name1".."branch_name2"</code>
* 두 개의 branch의 소스코드를 비교하는 명령어

## branch 병합

<code>git merge exp</code>
* exp를 현재있는 branch로 병합하려 할때 사용하는 명령어
    exp => master 하려면 일단 master에 checkout한 상태에서 해야한다

<code>git branch -d "branch_name"</code>
* 이미 Merge한 branch를 삭제하는 명령어

<code>git branch -D "branch_name"</code>
* Merge하지 않은 branch를 강제로 삭제하는 명령어


## branch 병합 시 충돌해결

2개의 branch에서 같은 곳을 변경하여 merge하면 충돌이 발생한다 이때 개발자가 직접 오류부분을 수정하여 merge하면 해결된다

## stash
다른 branch로 checkout을 해야 하는데 아직 현재 branch에서 작입이 끝나지 않은 경우에 사용하여 작업중이던 파일을 임시로 저장해두고 현재 brnach의 상태를 마지막 commit상태로 초기화 할 수 있다
<code>git stash</code>
* 현재 branch의 작업내용이 저장되고 마지막 commit상태로 초기화하는 명령어

<code>git stash apply</code>
* 저장하였던 작업내용을 불러오는 명령어

<code>git stash list</code>
* 저장된 stash목록을 보여주는 명령어

<code>git stash drop</code>
* 저장된 stash목록중 최신 stash를 삭제하는 명령어

<code>git stash pop</code>
* 저장된 stash 목록중 최신 stash를 적용하고 삭제하는 명령어