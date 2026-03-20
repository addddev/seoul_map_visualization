<!DOCTYPE html>
<html>
<head>
    <title>서울시 상권지도</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <!-- Map height -->
    <style>
        #mapid { height: 400px; }
    </style>
</head>
<body>

<h2>서울시 상권지도</h2>
<?php
    if (!isset($_GET['dong'])):  // 법정동이 선택되지 않았다면 시군구 선택 바를 표시합니다.
        $dictData1 = file_get_contents('/opt/lampp/htdocs/시군구_dict.json'); // TODO! 다운 받은 경로로 경로를 바꿔주세요!
        $dictArray1 = json_decode($dictData1, true);
        $count = 0;
    ?>

    <div class="row">
    <?php foreach ($dictArray1 as $district => $dongs): ?>
        <?php if ($count % 5 == 0 && $count != 0) echo '</div><div class="row">'; $count++; ?>
        <div class="col-md-2">
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <?php echo $district; ?>
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <!-- 법정동 바 -->
                    <?php foreach ($dongs as $dong): ?>
                        <a class="dropdown-item" href="?dong=<?php echo $dong; ?>"><?php echo $dong; ?></a>
                    <?php endforeach; ?>
                </div>
            </div>
        </div>
    <?php endforeach; ?>
    </div>

    <?php
    elseif (!isset($_GET['sub'])):  // 법정동만 선택되었다면 대분류 바를 표시합니다.
        $분류정보 = json_decode(file_get_contents('/opt/lampp/htdocs/소분류_dict.json'), true); // TODO! 다운 받은 경로로 경로를 바꿔주세요!
    ?>

    <!-- 대분류 바 -->
    <div class="btn-group">
    <?php foreach ($분류정보 as $대분류명 => $중분류들): ?>
        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <?php echo $대분류명; ?>
            </button>
            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <!-- 중분류 바 -->
                <?php foreach ($중분류들 as $중분류명 => $소분류들): ?>
                    <h6 class="dropdown-header"><?php echo $중분류명; ?></h6>
                    <!-- 소분류 바 -->
                    <?php foreach ($소분류들 as $소분류명): ?>
                        <a class="dropdown-item" href="?dong=<?php echo $_GET['dong']; ?>&sub=<?php echo $소분류명; ?>"><?php echo $소분류명; ?></a>
                    <?php endforeach; ?>
                <?php endforeach; ?>
            </div>
        </div>
    <?php endforeach; ?>
    </div>

    <?php
    elseif (!isset($_GET['radius'])):  // 법정동과 대분류만 선택되었다면 거리 입력 필드를 표시합니다.
    ?>

    <!-- 거리 입력 필드 -->
    <form action="" method="get">
        <input type="hidden" name="dong" value="<?php echo $_GET['dong']; ?>">
        <input type="hidden" name="sub" value="<?php echo $_GET['sub']; ?>">
        <label for="radius">거리(킬로미터):</label>
        <input type="text" id="radius" name="radius">
        <input type="submit" value="Submit">
    </form>

    <?php
    else:  // 법정동과 대분류, 거리 모두 선택되었다면 선택한 법정동과 대분류, 거리를 출력하고 파이썬 스크립트를 실행합니다.

        echo "선택한 법정동: " . $_GET['dong'] . "<br>";
        echo "선택한 대분류: " . $_GET['sub'] . "<br>";
        echo "선택한 거리(km): " . $_GET['radius'] . "<br>";
        $dong = $_GET['dong'];
        $sub = $_GET['sub'];
        $radius = $_GET['radius'];  // 거리 값을 받아옵니다.
        $filePath = "/home/addd/miniconda3/bin/python3 /opt/lampp/htdocs/addd_commercial_district.py $sub $dong $radius 2>&1";  // TODO! 여기서 var로 시작하는 파일 경로를 다운받은 경로로 바꿔주세요!
	$output = shell_exec($filePath);
	$output = preg_replace('/root\s+/', '', $output);  // 'root'와 그 뒤의 공백 문자를 제거합니다.

	$html_file_get_contents = trim($output);
        $html_content= file_get_contents($html_file_get_contents);
        if ($html_content === FALSE) {
            echo "선택하신 주소에 입력하신 분류의 상가가 없습니다!";
        } else {
            // 읽어온 HTML 파일의 내용을 출력합니다.
            echo $html_content;
        }
    endif;
    ?>
</div>

</body>
</html>

