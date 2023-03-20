
import unittest
import bashdown

class TestCliArgParser(unittest.TestCase):

    def test_content_processing(self):
        """
        Since the markdown to be processed contains no bash it should be 
        idetical once processed
        """
        markdown = [
                "# my title",
                "",
                "some text",
                "---",
                "More text",
                "## subtitle",
                "end",
                ]
        processed_markdown = bashdown.process_content(markdown)
        self.assertEqual(processed_markdown, markdown)

    def test_bash_processing(self):
        """
        When we include some bash to process
        """
        markdown = [
                "# This includes some bash\n",
                "\n",
                "```bash\n",
                "echo 'this is a test'\n",
                "```\n",
                "\n",
                "## subtitle\n",
                ]
        expected_markdown = [
                "# This includes some bash\n",
                "\n",
                "```bash\n",
                "echo 'this is a test'\n",
                "```\n",
                "\n```output\n'this is a test'\n",
                "```\n",
                "\n",
                "## subtitle\n",
                ]
        processed_markdown = bashdown.process_content(markdown)
        self.assertEqual(processed_markdown, expected_markdown)

if __name__ == "__main__":
    unittest.main()
