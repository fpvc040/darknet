from icrawler.builtin import GoogleImageCrawler
import argparse


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description = "Add keyword and dir to save in")
	parser.add_argument("--keyword", help = "string to lookup", type = str, dest = 'keyword')
	parser.add_argument("--int", type = int, help = "number of images", dest = 'int')
	parser.add_argument("--path", help = "path to save", dest = 'path')
	args = parser.parse_args()


	google_crawler = GoogleImageCrawler(
	    feeder_threads=1,
	    parser_threads=2,
	    downloader_threads=4,
	    storage={'root_dir': args.path})
	google_crawler.crawl(keyword=args.keyword, max_num=args.int, file_idx_offset=0)