# -*- encoding: utf-8 -*-
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'notebook/version'

Gem::Specification.new do |s|
  s.name        = 'notebook'
  s.version     = Notebook::VERSION
  s.date        = '2013-02-11'
  s.summary     = "Notebook"
  s.description = "A notebook gem to hold single-line notes"
  s.authors     = ["Juliet Kemp"]
  s.email       = 'juliet@earth.li'

  s.files       = `git ls-files`.split("\n")
  s.test_files  = `git ls-files test/*`.split("\n")
  s.executables = "notebook"
  s.homepage    = ""
end
