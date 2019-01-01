# CSS_Grid

- grid-template-columns

- grid-template-rows

- grid-gap

- grid-auto-rows
- grid-auto-columns
  값을 설정해도 추가된 요소들이 나오지 않는다 이유는 기본적으로 추가된 요소는 row로 설정되어 있기 때문이다
- grid-auot-flow
  기본설정은 row, flex-direction과 비슷

- grid-template-areas
  css에서 뭔가를 그릴 수 있게 해줌

###### 새로운 기능

- fr : fraction 가능한 최대한 공간을 차지하라는 뜻
- repeat(반복수, 크기): column, row등을 반복시켜줌

- minmax(최소값, 최대값)
  설정을 통해 object크기의 최소값과 최대값을 설정할 수 있다

- max-content
  사용할 수 있는 최대의 공간을 가지게 설정함
- min-content
  가장 적은 공간 만을 가지게 설정함

- auto-fit
  가능한 많은 object를 column에 채우게 설정함(반응형)
- auto-fill
  최대한 모아 column에 채우게 설정함
  content가 없어도 가능한 많은 cell로 column을 채움

- justify-content & align-content
  flex와 같음
- place-content
  align와 justify를 같이 사용할 수 있음

- justify-items & align-items
  container안에 있는 item들을 움직이는 명령어
  설정을 하지 않으면 기본적으로 container에 맞게 늘림

- grid-column & grid-row
  container의 시작점과 끝점을 설정할 수 있다

- start & end
  container의 시작점 또는 끝점을 개별적으로 설정할 수 있다

- line naming
  grid-template-columns & grid-template-rows에서 []를 통해 라인이름을 지정할 수 있다

- grid-auto-flow
  빈칸을 채우는 명령어

- span
  grid-column & grid-row에서 시작점과 끝점을 지정하는게 아닌 차지할 칸수를 설정하는 명령어

- grid-area: row-start/column-start/row-end/column-end

- justify-self & align-self & place-self
  하나의 아이템만 수정할때 사용하는 명령어
