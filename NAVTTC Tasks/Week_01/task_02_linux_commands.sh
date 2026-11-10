# Task 2 - Linux commands
# Run with:  bash task_02_linux_commands.sh
# It makes a playground folder so don't worry shutdown / restart / sudo / dpkg are only printed, your pc will stays on. :DD

echo "--- pwd (where am i) ---"
pwd

echo
echo "--- mkdir + cd ---"
mkdir -p playground
cd playground
pwd

echo
echo "--- touch (make empty files) ---"
touch a.txt b.txt notes.txt
ls

echo
echo "--- redirection (> writes, >> adds) ---"
echo "first line" > notes.txt
echo "second line" >> notes.txt
echo "third line" >> notes.txt
cat notes.txt

echo
echo "--- cat, head, more, less ---"
seq 1 30 > numbers.txt
head -n 5 numbers.txt
echo "(more and less need a real terminal to scroll, try: less numbers.txt)"

echo
echo "--- file (what type is this) ---"
file notes.txt
file /bin/bash

echo
echo "--- cp and mv ---"
cp notes.txt notes_copy.txt
mv notes_copy.txt renamed.txt
ls

echo
echo "--- alias ---"
alias ll='ls -l'
ll

echo
echo "--- chmod ---"
echo 'echo "hello from my script"' > hello.sh
chmod +x hello.sh
ls -l hello.sh
./hello.sh

echo
echo "--- bash and sh ---"
bash hello.sh
sh hello.sh

echo
echo "--- ps and kill ---"
sleep 60 &
pid=$!
echo "started sleep with pid $pid"
ps -p $pid
kill $pid
echo "killed it"

echo
echo "--- man (manual) ---"
echo "try: man ls   (press q to quit)"

echo
echo "--- nano ---"
echo "try: nano notes.txt   (ctrl+o save, ctrl+x exit)"

echo
echo "--- rm and rmdir ---"
rm a.txt b.txt renamed.txt
ls
cd ..
rm -r playground
echo "playground deleted"

echo
echo "--- commands you run by hand (not auto-run here) ---"
echo "sudo apt update && sudo apt upgrade   # update packages"
echo "dpkg -l | head                        # list installed packages"
echo "shutdown -h now                       # power off"
echo "shutdown -r now                       # restart"