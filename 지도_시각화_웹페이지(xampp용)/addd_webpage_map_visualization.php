<!DOCTYPE html>
<html>
<body onload="setEndAge()">

<h2>서울시 데이터 시각화</h2>

<form method="post" autocomplete="off">
  <label for="menu">메뉴:</label><br>
  <select id="menu" name="menu" onchange="toggleInputFields()">
    <option value="income">서울 소득지도</option>
    <option value="subway">지하철 승하차 인구</option>
    <option value="population">서울 생활인구</option>
  </select><br>

  <div id="hour-field" style="display:none;">
    <label for="hour">시간:</label><br>
    <select id="hour" name="hour">
      <?php
      for ($i = 0; $i <= 23; $i++) {
        echo "<option value='$i'>$i</option>";
      }
      ?>
    </select><br>
  </div>

  <div id="age-field" style="display:none;">
    <label for="start_age">시작 나이 선택:</label>
    <select name="start_age" id="start_age" onchange="setEndAge()">
     <option value="0">0</option>
     <option value="10">10</option>
     <option value="15">15</option>
     <option value="20">20</option>
     <option value="25">25</option>
     <option value="30">30</option>
     <option value="35">35</option>
     <option value="40">40</option>
     <option value="45">45</option>
     <option value="50">50</option>
     <option value="55">55</option>
     <option value="60">60</option>
     <option value="65">65</option>
     <option value="70">70</option>
    </select>

    <input type="hidden" name="end_age" id="end_age">

    <p id="message"></p>
  </div>

  <div id="gender-field" style="display:none;">
    <label for="gender">성별:</label><br>
    <select id="gender" name="gender">
      <option value="남자">남자</option>
      <option value="여자">여자</option>
    </select><br>
  </div>

  <input type="submit" value="Submit">
</form>
<script>
function setEndAge() {
  var startAge = document.getElementById("start_age").value;
  var endAge;
  if (startAge !== null && startAge !== "") {  // startAge가 null이 아니고 빈 문자열도 아닌 경우에만 로직을 실행
    if (parseInt(startAge) === 0) {    
        endAge = 9;
    } else {
      endAge = parseInt(startAge) + 4;
    }
    document.getElementById("end_age").value = endAge;
    document.getElementById("message").textContent = "종료 나이는 " + endAge + "세 입니다!";
  } else {
    document.getElementById("end_age").value = "";
    document.getElementById("message").textContent = "";
  }
}

function toggleInputFields() {
  var selectedMenu = document.getElementById("menu").value;
  var hourField = document.getElementById("hour-field");
  var ageField = document.getElementById("age-field");
  var genderField = document.getElementById("gender-field");

  if (selectedMenu === "population") {
    hourField.style.display = "block";
    ageField.style.display = "block";
    genderField.style.display = "block";
  } else {
    hourField.style.display = "none";
    ageField.style.display = "none";
    genderField.style.display = "none";
  }
}

toggleInputFields();  // 페이지 로드 시 입력 필드 표시 여부 설정
</script>

</body>
</html>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $hour = $_POST['hour'];
    $start_age = $_POST['start_age'];
    $end_age = $_POST['end_age'];
    $gender = $_POST['gender'];
    $menu = $_POST['menu'];  // 메뉴 선택 값

    // TODO 메뉴 선택에 따른 파이썬 스크립트 실행(py파일 저장경로로 바꿔주세요!)
    if ($menu === "population") {
        echo "선택한 시간: $hour<br>";
        echo "시작 나이: $start_age<br>";
        echo "종료 나이: $end_age<br>";
        echo "성별: $gender<br>";

        $command = "/home/addd/miniconda3/bin/python3 /opt/lampp/htdocs/addd_webpage_map_visualization.py $hour $start_age $end_age $gender 2>&1";
    } elseif ($menu === "subway") {
        $command = "/home/addd/miniconda3/bin/python3 /opt/lampp/htdocs/addd_webpage_map_visualization_subway.py 2>&1";
    } elseif ($menu === "income") {
        $command = "/home/addd/miniconda3/bin/python3 /opt/lampp/htdocs/addd_webpage_map_visualization_income.py 2>&1";
    }

    $output = shell_exec($command);

    // 파이썬 스크립트가 반환한 출력물을 사용하여 HTML 파일의 경로를 얻습니다
    $html_file_path =trim($output);

    // HTML 파일이 존재하는지 확인합니다
    if (file_exists($html_file_path)) {
        // HTML 파일의 내용을 로드합니다
        $html_content = file_get_contents($html_file_path);

        // HTML 파일의 내용을 출력합니다
        echo $html_content;
    } else {
        echo "Error: File $html_file_path does not exist.";
    }
}
?>


