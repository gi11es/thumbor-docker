from . import WikimediaTestCase


class WikimediaVipsTest(WikimediaTestCase):
    def get_config(self):
        cfg = super(WikimediaVipsTest, self).get_config()
        cfg.VIPS_ENGINE_MIN_PIXELS = 0

        return cfg

    def test_tiff(self):
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(jpg)/0729.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-0729.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-0729.tiff.png',
            expected_width=400,
            expected_height=254,
            expected_ssim=0.95,
            size_tolerance=0.61,
        )
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(webp)/0729.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-0729.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-0729.tiff.png',
            expected_width=400,
            expected_height=254,
            expected_ssim=0.98,
            size_tolerance=1.12,
        )

    def test_multipage_tiff(self):
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(jpg):page(3)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page3-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page3-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.99,
            size_tolerance=0.8,
        )
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(webp):page(3)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page3-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page3-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.98,
            size_tolerance=0.66,
        )

    def test_multipage_tiff_without_page_filter(self):
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(jpg)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.99,
            size_tolerance=0.77,
        )
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(webp)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.98,
            size_tolerance=0.66,
        )

    def test_multipage_tiff_with_out_of_bounds_page(self):
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(jpg):page(500)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.99,
            size_tolerance=0.77,
        )
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(webp):page(500)/International_Convention_for_Regulation_of_Whaling.tiff',
            mediawiki_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.jpg',
            perfect_reference_thumbnail='lossy-page1-400px-International_Convention_for_Regulation_of_Whaling.tiff.png',
            expected_width=400,
            expected_height=566,
            expected_ssim=0.98,
            size_tolerance=0.66,
        )

    def test_tiff_with_invalid_icc_profile(self):
        self.run_and_check_ssim_and_size(
            url=(
                '/thumbor/unsafe/400x/filters:format(jpg)/Julia_Margaret_'
                'Cameron_-_Queen_of_the_May_-_1984.166_-_Cleveland_Museum_of_Art.tif'
            ),
            mediawiki_reference_thumbnail=(
                'lossy-page1-400px-Julia_Margaret_Cameron_-_Queen_of_the_May_'
                '-_1984.166_-_Cleveland_Museum_of_Art.tif.jpg'
            ),
            perfect_reference_thumbnail=(
                'lossy-page1-400px-Julia_Margaret_Cameron_-_Queen_of_the_May_'
                '-_1984.166_-_Cleveland_Museum_of_Art.tif.png'
            ),
            expected_width=400,
            expected_height=527,
            expected_ssim=0.97,
            size_tolerance=0.6,
        )
        self.run_and_check_ssim_and_size(
            url=(
                '/thumbor/unsafe/400x/filters:format(webp)/Julia_Margaret_'
                'Cameron_-_Queen_of_the_May_-_1984.166_-_Cleveland_Museum_of_Art.tif'
            ),
            mediawiki_reference_thumbnail=(
                'lossy-page1-400px-Julia_Margaret_Cameron_-_Queen_of_the_May_'
                '-_1984.166_-_Cleveland_Museum_of_Art.tif.webp'
            ),
            perfect_reference_thumbnail=(
                'lossy-page1-400px-Julia_Margaret_Cameron_-_Queen_of_the_May_'
                '-_1984.166_-_Cleveland_Museum_of_Art.tif.png'
            ),
            expected_width=400,
            expected_height=527,
            expected_ssim=0.97,
            size_tolerance=1.0,
        )

    def test_png(self):
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(png)/WorldMap-A_non-Frame.png',
            mediawiki_reference_thumbnail='400px-WorldMap-A_non-Frame.png',
            perfect_reference_thumbnail='400px-WorldMap-A_non-Frame.png',
            expected_width=400,
            expected_height=200,
            expected_ssim=0.98,
            size_tolerance=1.1,
        )
        self.run_and_check_ssim_and_size(
            url='/thumbor/unsafe/400x/filters:format(webp)/WorldMap-A_non-Frame.png',
            mediawiki_reference_thumbnail='400px-WorldMap-A_non-Frame.png',
            perfect_reference_thumbnail='400px-WorldMap-A_non-Frame.png',
            expected_width=400,
            expected_height=200,
            expected_ssim=0.98,
            size_tolerance=0.84,
        )

    def test_skip_factor_1(self):
        self.run_and_check_ssim_and_size(
            url=(
                '/thumbor/unsafe/2000x/filters:format(png)/'
                'Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            mediawiki_reference_thumbnail=(
                '2000px-Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            perfect_reference_thumbnail=(
                '2000px-Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            expected_width=2000,
            expected_height=987,
            expected_ssim=0.99,
            size_tolerance=1.01,
        )
        self.run_and_check_ssim_and_size(
            url=(
                '/thumbor/unsafe/2000x/filters:format(webp)/'
                'Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            mediawiki_reference_thumbnail=(
                '2000px-Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            perfect_reference_thumbnail=(
                '2000px-Lakedaimoniergrab_Zeichnung_und_Steinplan.png'
            ),
            expected_width=2000,
            expected_height=987,
            expected_ssim=0.99,
            size_tolerance=0.88,
        )
