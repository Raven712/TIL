# JS Event

- '~하면 ~ 한다' 라는 의미를 가짐.
  - 이벤트 발생시 특정함수가 등록(실행)된다.



```javascript
<button id='btn'>버튼</button>
<p id='counter'>0</p>
<script>
    const btn = document.querySelector('#btn')
	console.log(btn)
	btn.addEventListener('click', function() { console.log('버튼 클릭') })
//클릭이 되면 console.log('버튼 클릭')이 실행됨.
	btn.addEventlistener('click', function() { console.log('클릭')
                                             countNumber += 1
                                             //countNumber 증가시키고
                                             const counter = document.querySelector('#counter')
                                             counter.innerText = countNumber})
```



```js
<input type='text' id='text-input'>
<script>
    const textInput = document.querySelector('#text-input')
// 1. input 선택
	textInput.addEventListener('input', function(event) {
        // 입력된 내용 받아오기. input 은 이벤트의 대상
        console.log(event)
        
    })
```

