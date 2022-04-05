while IFS="" read -r file || [ -n "$file" ]
do
  rm -rf $file
done < .deployignore