cd content
for i in *.rst; do
  restructuredtext-lint "$i"
  if [ $? != 0 ]; then
     exit $?
  fi
done
exit 0
