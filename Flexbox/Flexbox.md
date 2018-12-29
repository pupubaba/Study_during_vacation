# flexbox
flex옵션을 주면 기본적으로 flex-direction: row라는 옵션을 가짐
### justify-content
main axis는 justify-content가 영향을 주는 축
justify-content :  
                    flex-start: 요소들을 컨테이너의 왼쪽으로 정렬
                    flex-end: 요소들을 컨테이너의 오른쪽으로 정렬
                    center: 요소들을 컨테이너의 가운데로 정렬
                    space-between: 요소들 사이에 동일한 간격을 둠
                    space-around: 요소들 주위에 동일한 간격을 둠
### align-items
align-items를 사용하기 위해서는 충분한 높이가 있어야 작동함
cross axis는 align-items가 영향을 주는 축
align-items :
                flex-start: 요소들을 컨테이너의 꼭대기로 정렬
                flex-end: 요소들을 컨테이너의 바닥으로 정렬
                center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬
                baseline: 요소들을 컨테이너의 시작 위치에 정렬
                stretch: 요소들을 컨테이너에 맞도록 늘림
### flex-direction
row이면 main axis는 수평축
column이면 main axis는 수직축

row: 요소들을 텍스트의 방향과 동일하게 정렬
row-reverse: 요소들을 텍스트의 반대 방향으로 정렬
column: 요소들을 위에서 아래로 정렬
column-reverse: 요소들을 아래에서 위로 정렬
reverse를 사용하면 요소들의 start와 end의 순서도 뒤바뀝니다.
flex의 방향이 column일 경우 justify-content의 방향이 세로로, align-items의 방향이 가로로 바뀝니다.

### align-content
세로선 상에 여분의 공간이 있는 경우 flex 컨테이너 사이의 간격을 조절함
flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬
flex-end: 여러 줄들을 컨테이너의 바닥에 정렬
center: 여러 줄들을 세로선 상의 가운데에 정렬
space-between: 여러 줄들 사이에 동일한 간격을 둠
space-around: 여러 줄들 주위에 동일한 간격을 둠
stretch: 여러 줄들을 컨테이너에 맞도록 늘림

### flex-wrap
아이템들 사이에 더이상 공간이 없을때 flexbox가 해야 할 행동들을 정의할 수 있음
wrap을 하고 있지 않을때 flexbox는 아이템들을 최대한 압축해서 한 줄에 모든 아이템들이 들어오도록 함
기본 설정은 nowrap

### align-self
flex-container에 주는 대신 flex-item에 직접 옵션을 줘서 각각에 item을 설정할 수 있다

### order
flex item의 배치 순서를 제어하는 속성으로 기본값은 0이고 flex-direction속성의 방향값을 기준으로 낮은 숫자를 먼저 배치하고 높은 숫자를 나중에 배치한다