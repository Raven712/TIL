# JS 1일_Event(2) 버블링

- h1을 클릭한다고 해도, 사실 window,document,html,body,div 전부 클릭하는게 된다
- event가 캡처링(window->document->...->h1) 돼서 h1이 타겟이 됐다고 하는거임
  - 반대는 버블링(h1->...->window)



## modal

- 모달이 켜졌을때의 클래스를 만들어두고,
- 이벤트가 발동되었을때 모달이 작동하도록 하자

```html
  <style>
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      background-color: rgba(0, 0, 0, 0.7);
      /* a는 alpha로 투명도를 뜻함 */
      width: 100%;
      height: 100vh; 
      /* 전체 뷰포트 (100vh) */
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      display: none;
    }
    .modal-active {
      display: flex;
    }
    .modal-deactive {
      display: none;
    }
  </style>
</head>
<body>
  <button id="btn-modal">모달버튼</button>
  <div class="modal-overlay" id="modal-content">
    모달창
    <button id="modal-quit">모달 끄기</button>
  </div>
  <script>
    const modalBtn = document.querySelector('#btn-modal')
    // 일단 선언을 하고
    modalBtn.addEventListener('click', function(event){
      // 모달버튼이 클릭이 되면 display: none을 display: flex;로 바꾸자 --> 그러므로 active 클래스를 만들어서, 클래스를 켰다 껐다 하게하면된다
      // 켰다껐다 --> 토글!
      document.querySelector('#modal-content').classList.toggle('modal-active')
    const modalquitBtn = document.querySelector('#modal-quit')
    // 모달 취소버튼 선언
    modalquitBtn.addEventListener('click', function(){
      document.querySelector('#modal-content').classList.toggle('modal-deactive')
    })
    })
  </script>
</body>
```

