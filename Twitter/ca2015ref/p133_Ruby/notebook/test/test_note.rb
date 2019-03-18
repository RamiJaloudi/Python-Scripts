require 'test/unit'
require 'shoulda'
require_relative '../lib/notebook/note'

class TestNote < Test::Unit::TestCase
    
  context "With notes" do
      setup do
          @title = "test_title"
          @body = "test_body"
          @new_title = "new title"
          @test_note = Notebook::Note.new(@title, @body)
          @notebook = "notebook.txt"
      end

      should "output title and body string for to_s" do
        assert_equal "#{@title},#{@body}", @test_note.to_s
      end

      should "have last line of file equal to test note values after write_to_file" do
          @test_note.write_to_file(@notebook)
          @last_line = `tail -n 1 #{@notebook}`
          assert_equal "#{@title},#{@body}", @last_line.chomp
      end

      should "change title from test to 'new title'" do
          @test_note.edit_title(@new_title)
          assert_equal @new_title, @test_note.title
      end

      should "mark as done" do
          @test_note.mark_as_done
          assert_equal "DONE " + @title, @test_note.title
      end
  end
end

