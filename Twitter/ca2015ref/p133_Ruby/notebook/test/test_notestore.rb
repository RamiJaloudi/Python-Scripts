require 'test/unit'
require 'shoulda'
require_relative '../lib/notebook/notestore'
require_relative '../lib/notebook/note'

class TestNoteStore < Test::Unit::TestCase

    context "With notes" do
        setup do
            @title = "test_title"
            @newtitle = "NEWTITLE"
            @body = "test_body"
            @note = Notebook::Note.new(@title, @body)
            @note2 = Notebook::Note.new(@title, @body)
        end

        should "Have note when note added then none when deleted" do
            Notebook::NoteStore.instance.add(@note)
            assert_equal [@note], Notebook::NoteStore.instance.notebook_array
            Notebook::NoteStore.instance.delete(0)
            assert_equal [], Notebook::NoteStore.instance.notebook_array
        end

        should "Run do_to_all correctly" do
            Notebook::NoteStore.instance.add(@note)
            Notebook::NoteStore.instance.add(@note2)
            Notebook::NoteStore.instance.do_to_all do |n|
                n.edit_title(@newtitle)
            end
            assert_equal [@note, @note2], Notebook::NoteStore.instance.notebook_array
        end

    end
end

