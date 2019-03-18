require 'test/unit'
require 'shoulda'
require_relative '../lib/notebook/reader'
require_relative '../lib/notebook/note'
require_relative '../lib/notebook/notestore'

class TestReader < Test::Unit::TestCase

  context "read" do
      setup do
        @test_file = "testfile"
        @note = "Test Note,test body"
      end

      should "return test file contents when reading test file" do
        File.open(@test_file, 'w') {|f| f.write(@note) }
        reader = Notebook::Reader.new(@test_file)
        assert_equal Notebook::NoteStore.instance.output, reader.read
        File.delete(@test_file)
      end 
  end 
end

