require 'test/unit'
require 'shoulda'
require_relative '../lib/notebook/options'

class TestOptions < Test::Unit::TestCase
  
  context "specifying no notebook" do
    should "return default" do
      opts = Notebook::Options.new([])
      assert_equal Notebook::Options::DEFAULT_NOTEBOOK, opts.notebook
    end
  end

  context "specifying a notebook" do
    should "return it" do
      opts = Notebook::Options.new(["-n", "test_notebook"])
      assert_equal "test_notebook", opts.notebook
    end
  end

  context "specifying do to all" do
    should "return all and new title" do
      opts = Notebook::Options.new(["-x", "NEWTITLE"])
      assert_equal true, opts.all
      assert_equal "NEWTITLE", opts.all_title
    end
  end


  context "specifying edit" do
    should "return edit and edit number" do
      opts = Notebook::Options.new(["-e", "2"])
      assert_equal 2, opts.edit_number
      assert_equal true, opts.edit
    end
  end

  context "specifying read" do
    should "return read" do
      opts = Notebook::Options.new(["-r"])
      assert_equal true, opts.read
    end
  end

  context "specifying add" do
    should "return add" do
      opts = Notebook::Options.new(["-a"])
      assert_equal true, opts.add
    end
  end

end

