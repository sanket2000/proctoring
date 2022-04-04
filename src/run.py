import audio
import head_pose
import detection
import threading as th


if __name__ == "__main__":
    # main()
    t1 = th.Thread(target=head_pose.pose)
    t2 = th.Thread(target=audio.sound)
    t3 = th.Thread(target=detection.run_detection)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
